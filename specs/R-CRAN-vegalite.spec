%global __brp_check_rpaths %{nil}
%global packname  vegalite
%global packver   0.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.1
Release:          3%{?dist}%{?buildtag}
Summary:          Tools to Encode Visualizations with the 'Grammar ofGraphics'-Like 'Vega-Lite' 'Spec'

License:          AGPL + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-htmlwidgets >= 0.6
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-clipr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-webshot 
BuildRequires:    R-CRAN-base64 
BuildRequires:    R-stats 
Requires:         R-CRAN-htmlwidgets >= 0.6
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-digest 
Requires:         R-tools 
Requires:         R-CRAN-clipr 
Requires:         R-utils 
Requires:         R-CRAN-webshot 
Requires:         R-CRAN-base64 
Requires:         R-stats 

%description
The 'Vega-Lite' 'JavaScript' framework provides a higher-level grammar for
visual analysis, akin to 'ggplot' or 'Tableau', that generates complete
'Vega' specifications. Functions exist which enable building a valid
'spec' from scratch or importing a previously created 'spec' file.
Functions also exist to export 'spec' files and to generate code which
will enable plots to be embedded in properly configured web pages. The
default behavior is to generate an 'htmlwidget'.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
