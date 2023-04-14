%global __brp_check_rpaths %{nil}
%global packname  brlrmr
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          3%{?dist}%{?buildtag}
Summary:          Bias Reduction with Missing Binary Response

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-brglm 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-profileModel 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
Requires:         R-boot 
Requires:         R-CRAN-brglm 
Requires:         R-MASS 
Requires:         R-CRAN-profileModel 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 

%description
Provides two main functions, il() and fil(). The il() function implements
the EM algorithm developed by Ibrahim and Lipsitz (1996)
<DOI:10.2307/2533068> to estimate the parameters of a logistic regression
model with the missing response when the missing data mechanism is
nonignorable. The fil() function implements the algorithm proposed by
Maity et. al. (2017+) <https://github.com/arnabkrmaity/brlrmr> to reduce
the bias produced by the method of Ibrahim and Lipsitz (1996)
<DOI:10.2307/2533068>.

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
