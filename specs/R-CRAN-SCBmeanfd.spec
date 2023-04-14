%global __brp_check_rpaths %{nil}
%global packname  SCBmeanfd
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          3%{?dist}%{?buildtag}
Summary:          Simultaneous Confidence Bands for the Mean of Functional Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-boot 
BuildRequires:    R-KernSmooth 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-boot 
Requires:         R-KernSmooth 

%description
Statistical methods for estimating and inferring the mean of functional
data. The methods include simultaneous confidence bands, local polynomial
fitting, bandwidth selection by plug-in and cross-validation,
goodness-of-fit tests for parametric models, equality tests for two-sample
problems, and plotting functions.

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
