%global packname  fpp2
%global packver   2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3
Release:          2%{?dist}
Summary:          Data for "Forecasting: Principles and Practice" (2nd Edition)

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast >= 8.3
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-fma 
BuildRequires:    R-CRAN-expsmooth 
Requires:         R-CRAN-forecast >= 8.3
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-fma 
Requires:         R-CRAN-expsmooth 

%description
All data sets required for the examples and exercises in the book
"Forecasting: principles and practice" by Rob J Hyndman and George
Athanasopoulos <https://OTexts.org/fpp2/>. All packages required to run
the examples are also loaded.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
