%global __brp_check_rpaths %{nil}
%global packname  spearmanCI
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Jackknife Euclidean / Empirical Likelihood Inference forSpearman's Rho

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-emplik 
BuildRequires:    R-MASS 
Requires:         R-CRAN-emplik 
Requires:         R-MASS 

%description
Functions for conducting jackknife Euclidean / empirical likelihood
inference for Spearman's rho (de Carvalho and Marques (2012)
<10.1080/10920277.2012.10597644>).

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
