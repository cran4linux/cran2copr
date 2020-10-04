%global packname  NHMSAR
%global packver   1.17
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.17
Release:          3%{?dist}%{?buildtag}
Summary:          Non-Homogeneous Markov Switching Autoregressive Models

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ucminf 
BuildRequires:    R-CRAN-lars 
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-CRAN-ncvreg 
Requires:         R-CRAN-ucminf 
Requires:         R-CRAN-lars 
Requires:         R-CRAN-glasso 
Requires:         R-CRAN-ncvreg 

%description
Calibration, simulation, validation of (non-)homogeneous Markov switching
autoregressive models with Gaussian or von Mises innovations.
Penalization methods are implemented for Markov Switching Vector
Autoregressive Models of order 1 only. Most functions of the package
handle missing values.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
