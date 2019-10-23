%global packname  flood
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Statistical Methods for the (Regional) Analysis of FloodFrequency

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-CRAN-TLMoments 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-copula 
Requires:         R-CRAN-evd 
Requires:         R-CRAN-TLMoments 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-copula 

%description
Includes several statistical methods for the estimation of parameters and
high quantiles of river flow distributions. The focus is on regional
estimation based on homogeneity assumptions and computed from multivariate
observations (multiple measurement stations). For details see Kinsvater et
al. (2017) <arXiv:1701.06455>.

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
