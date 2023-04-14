%global __brp_check_rpaths %{nil}
%global packname  tpAUC
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Estimation and Inference of Two-Way pAUC, pAUC and pODC

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-pROC 
Requires:         R-stats 
Requires:         R-graphics 

%description
Tools for estimating and inferring two-way partial area under receiver
operating characteristic curves (two-way pAUC), partial area under
receiver operating characteristic curves (pAUC), and partial area under
ordinal dominance curves (pODC). Methods includes Mann-Whitney statistic
and Jackknife, etc.

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
