%global __brp_check_rpaths %{nil}
%global packname  LPower
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Calculates Power, Sample Size, or Detectable Effect forLongitudinal Analyses

License:          Unlimited
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-nlme 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
Requires:         R-nlme 
Requires:         R-MASS 
Requires:         R-stats 

%description
Computes power, or sample size or the detectable difference for a repeated
measures model with attrition. It requires the variance covariance matrix
of the observations but can compute this matrix for several common random
effects models. See Diggle, P, Liang, KY and Zeger, SL (1994,
ISBN:9780198522843).

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
