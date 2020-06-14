%global packname  ssev
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Sample Size Computation for Fixed N with Optimal Reward

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-pwr 
BuildRequires:    R-CRAN-MESS 
BuildRequires:    R-stats 
Requires:         R-CRAN-pwr 
Requires:         R-CRAN-MESS 
Requires:         R-stats 

%description
Computes the optimal sample size for various 2-group designs (e.g., when
comparing the means of two groups assuming equal variances, unequal
variances, or comparing proportions) when the aim is to maximize the
rewards over the full decision procedure of a) running a trial (with the
computed sample size), and b) subsequently administering the winning
treatment to the remaining N-n units in the population. Sample sizes and
expected rewards for standard t- and z- tests are also provided.

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
%{rlibdir}/%{packname}/INDEX
