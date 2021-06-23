%global __brp_check_rpaths %{nil}
%global packname  ProFit
%global packver   1.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.3
Release:          3%{?dist}%{?buildtag}
Summary:          Fit Projected 2D Profiles to Galaxy Images

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildRequires:    R-CRAN-magicaxis >= 2.0.3
BuildRequires:    R-CRAN-celestial >= 1.4.1
BuildRequires:    R-CRAN-FITSio 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-LaplacesDemon 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-checkmate 
Requires:         R-CRAN-magicaxis >= 2.0.3
Requires:         R-CRAN-celestial >= 1.4.1
Requires:         R-CRAN-FITSio 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-LaplacesDemon 
Requires:         R-methods 
Requires:         R-CRAN-checkmate 

%description
Get data / Define model / ??? / Profit! 'ProFit' is a Bayesian galaxy
fitting tool that uses a fast 'C++' image generation library and a
flexible interface to a large number of likelihood samplers.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/vignettes-nonCRAN
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
