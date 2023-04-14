%global __brp_check_rpaths %{nil}
%global packname  ggwordcloud
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          3%{?dist}%{?buildtag}
Summary:          A Word Cloud Geom for 'ggplot2'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-scales >= 1.0.0
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-png 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-scales >= 1.0.0
Requires:         R-grid 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-png 

%description
Provides a word cloud text geom for 'ggplot2'. Texts are placed so that
they do not overlap as in 'ggrepel'.  The algorithm used is a variation
around the one of 'wordcloud2.js'.

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
