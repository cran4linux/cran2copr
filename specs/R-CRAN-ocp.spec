%global __brp_check_rpaths %{nil}
%global packname  ocp
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Online Changepoint Detection

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-grid >= 3.4.0
BuildRequires:    R-graphics >= 3.4.0
BuildRequires:    R-grDevices >= 3.4.0
Requires:         R-grid >= 3.4.0
Requires:         R-graphics >= 3.4.0
Requires:         R-grDevices >= 3.4.0

%description
Implements the Bayesian online changepoint detection method by Adams and
MacKay (2007) <arXiv:0710.3742> for univariate or multivariate data.
Gaussian and Poisson probability models are implemented. Provides
post-processing functions with alternative ways to extract changepoints.

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
