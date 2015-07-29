module.exports = function(grunt) {

  var static_files = 'static';
  var scss_files = 'scss';
  var bower_components = 'bower_components';

  // Project configuration.
  grunt.initConfig({

    concat: {
      js_header: {
        src: [bower_components + '/modernizr/modernizr.js'],
        dest: static_files + '/js/output_header.js',
      },
      js_footer: {
        src: [bower_components + '/jquery/dist/jquery.min.js', bower_components + '/fastclick/lib/fastclick.js', bower_components + '/foundation/js/foundation.min.js'],
        dest: static_files + '/js/output_footer.js',
      },
    },

    sass: {
      dist: {
        files: [
            {src: [scss_files + '/app.scss'], dest: static_files + '/css/output.css'},
        ],
      },
    },

    copy: {
      jquery_map : {
        files: [
          {expand: true, cwd: bower_components + '/jquery/dist/', src: ['jquery.min.map'], dest: static_files + '/js'},
        ],
      },
      font_awesome_fonts: {
        files: [
            {expand: true, cwd: bower_components + '/font-awesome/fonts', src: ['*'], dest: static_files + '/fonts'},
        ],
      },
    },

    uglify: {
      js_header: {
        src: static_files + '/js/output_header.js',
        dest: static_files + '/js/output_header.js',
      },
      js_footer: {
        src: static_files + '/js/output_footer.js',
        dest: static_files + '/js/output_footer.js',
      },
    },

    cssmin: {
      css: {
        src: static_files + '/css/output.css',
        dest: static_files + '/css/output.css',
      },
    },

    watch: {
      js: {
        files: [bower_components + '/**.js', bower_components + '/**.map'],
        tasks: ['concat', 'copy'],
      },
      sass: {
        files: [scss_files + '/**.scss', scss_files + '/**/*.scss', bower_components + 'foundation/scss/**.scss'],
        tasks: ['sass'],
      },
    },

  });

  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-cssmin');

  grunt.registerTask('default', ['concat', 'sass', 'uglify', 'cssmin', 'copy', 'watch']);
};
