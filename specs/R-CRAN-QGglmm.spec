%global __brp_check_rpaths %{nil}
%global packname  QGglmm
%global packver   0.7.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.4
Release:          3%{?dist}%{?buildtag}
Summary:          Estimate Quantitative Genetics Parameters from GeneralisedLinear Mixed Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cubature >= 1.4
Requires:         R-CRAN-cubature >= 1.4

%description
Compute various quantitative genetics parameters from a Generalised Linear
Mixed Model (GLMM) estimates. Especially, it yields the observed
phenotypic mean, phenotypic variance and additive genetic variance.

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
