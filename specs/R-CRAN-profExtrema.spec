%global packname  profExtrema
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          3%{?dist}
Summary:          Compute and Visualize Profile Extrema Functions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-DiceKriging 
BuildRequires:    R-CRAN-KrigInv 
BuildRequires:    R-CRAN-pGPx 
BuildRequires:    R-CRAN-microbenchmark 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-lhs 
BuildRequires:    R-splines 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-utils 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-rcdd 
Requires:         R-CRAN-DiceKriging 
Requires:         R-CRAN-KrigInv 
Requires:         R-CRAN-pGPx 
Requires:         R-CRAN-microbenchmark 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-lhs 
Requires:         R-splines 
Requires:         R-methods 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-utils 
Requires:         R-MASS 
Requires:         R-CRAN-rcdd 

%description
Computes profile extrema functions for arbitrary functions. If the
function is expensive-to-evaluate it computes profile extrema by emulating
the function with a Gaussian process (using package 'DiceKriging'). In
this case uncertainty quantification on the profile extrema can also be
computed. The different plotting functions for profile extrema give the
user a tool to better locate excursion sets.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
