%global packname  CompDist
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Multisection Composite Distributions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-fExtremes 
BuildRequires:    R-CRAN-actuar 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-rmutil 
BuildRequires:    R-CRAN-PearsonDS 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-fExtremes 
Requires:         R-CRAN-actuar 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-rmutil 
Requires:         R-CRAN-PearsonDS 

%description
Computes density function, cumulative distribution function, quantile
function and random numbers for a multisection composite distribution
specified by the user.  Also fits the user specified distribution to a
given data set.  More details of the package can be found in the following
paper submitted to the R journal Wiegand M and Nadarajah S (2017)
CompDist: Multisection composite distributions.

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
%{rlibdir}/%{packname}/INDEX
