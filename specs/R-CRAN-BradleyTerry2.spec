%global __brp_check_rpaths %{nil}
%global packname  BradleyTerry2
%global packver   1.1-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Bradley-Terry Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 >= 1.0
BuildRequires:    R-CRAN-brglm 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-qvcalc 
BuildRequires:    R-stats 
Requires:         R-CRAN-lme4 >= 1.0
Requires:         R-CRAN-brglm 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-qvcalc 
Requires:         R-stats 

%description
Specify and fit the Bradley-Terry model, including structured versions in
which the parameters are related to explanatory variables through a linear
predictor and versions with contest-specific effects, such as a home
advantage.

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
