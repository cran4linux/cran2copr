%global packname  relaimpo
%global packver   2.2-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.3
Release:          1%{?dist}
Summary:          Relative Importance of Regressors in Linear Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.2.1
Requires:         R-core >= 2.2.1
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-mitools 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-corpcor 
Requires:         R-MASS 
Requires:         R-boot 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-mitools 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-corpcor 

%description
Provides several metrics for assessing relative importance in linear
models. These can be printed, plotted and bootstrapped. The recommended
metric is lmg, which provides a decomposition of the model explained
variance into non-negative contributions. There is a version of this
package available that additionally provides a new and also recommended
metric called pmvd. If you are a non-US user, you can download this
extended version from Ulrike Groempings web site.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
