%global __brp_check_rpaths %{nil}
%global packname  snfa
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Smooth Non-Parametric Frontier Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-prodlim >= 2018.4.18
BuildRequires:    R-CRAN-rootSolve >= 1.7
BuildRequires:    R-CRAN-quadprog >= 1.5.5
BuildRequires:    R-CRAN-abind >= 1.4.5
BuildRequires:    R-CRAN-Rdpack >= 0.10.1
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-prodlim >= 2018.4.18
Requires:         R-CRAN-rootSolve >= 1.7
Requires:         R-CRAN-quadprog >= 1.5.5
Requires:         R-CRAN-abind >= 1.4.5
Requires:         R-CRAN-Rdpack >= 0.10.1

%description
Fitting of non-parametric production frontiers for use in efficiency
analysis. Methods are provided for both a smooth analogue of Data
Envelopment Analysis (DEA) and a non-parametric analogue of Stochastic
Frontier Analysis (SFA). Frontiers are constructed for multiple inputs and
a single output using constrained kernel smoothing as in Racine et al.
(2009), which allow for the imposition of monotonicity and concavity
constraints on the estimated frontier.

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
