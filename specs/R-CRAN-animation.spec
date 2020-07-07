%global packname  animation
%global packver   2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.6
Release:          3%{?dist}
Summary:          A Gallery of Animations in Statistics and Utilities to CreateAnimations

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         ImageMagick
Requires:         tex(latex)
BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-magick 
Requires:         R-CRAN-magick 

%description
Provides functions for animations in statistics, covering topics in
probability theory, mathematical statistics, multivariate statistics,
non-parametric statistics, sampling survey, linear models, time series,
computational statistics, data mining and machine learning. These
functions may be helpful in teaching statistics and data analysis. Also
provided in this package are a series of functions to save animations to
various formats, e.g. Flash, 'GIF', HTML pages, 'PDF' and videos. 'PDF'
animations can be inserted into 'Sweave' / 'knitr' easily.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/articles
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/misc
%{rlibdir}/%{packname}/INDEX
