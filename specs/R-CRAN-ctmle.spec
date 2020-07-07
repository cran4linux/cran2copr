%global packname  ctmle
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}
Summary:          Collaborative Targeted Maximum Likelihood Estimation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-SuperLearner 
BuildRequires:    R-CRAN-tmle 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-stats 
Requires:         R-CRAN-SuperLearner 
Requires:         R-CRAN-tmle 
Requires:         R-CRAN-glmnet 
Requires:         R-stats 

%description
Implements the general template for collaborative targeted maximum
likelihood estimation. It also provides several commonly used C-TMLE
instantiation, like the vanilla/scalable variable-selection C-TMLE (Ju et
al. (2017) <doi:10.1177/0962280217729845>) and the glmnet-C-TMLE algorithm
(Ju et al. (2017) <arXiv:1706.10029>).

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
