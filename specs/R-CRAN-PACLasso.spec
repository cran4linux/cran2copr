%global __brp_check_rpaths %{nil}
%global packname  PACLasso
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Penalized and Constrained Lasso Optimization

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3
BuildRequires:    R-methods >= 3.4.4
BuildRequires:    R-CRAN-limSolve >= 1.5.5.3
BuildRequires:    R-CRAN-quadprog >= 1.5
BuildRequires:    R-CRAN-lars >= 1.2
BuildRequires:    R-CRAN-penalized >= 0.9
Requires:         R-MASS >= 7.3
Requires:         R-methods >= 3.4.4
Requires:         R-CRAN-limSolve >= 1.5.5.3
Requires:         R-CRAN-quadprog >= 1.5
Requires:         R-CRAN-lars >= 1.2
Requires:         R-CRAN-penalized >= 0.9

%description
An implementation of both the equality and inequality constrained lasso
functions for the algorithm described in "Penalized and Constrained
Optimization" by James, Paulson, and Rusmevichientong (Journal of the
American Statistical Association, 2019; see
<http://www-bcf.usc.edu/~gareth/research/PAC.pdf> for a full-text version
of the paper). The algorithm here is designed to allow users to define
linear constraints (either equality or inequality constraints) and use a
penalized regression approach to solve the constrained problem. The
functions here are used specifically for constraints with the lasso
formulation, but the method described in the PaC paper can be used for a
variety of scenarios. In addition to the simple examples included here
with the corresponding functions, complete code to entirely reproduce the
results of the paper is available online through the Journal of the
American Statistical Association.

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
