%global packname  moko
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          2%{?dist}
Summary:          Multi-Objective Kriging Optimization

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-methods >= 3.0.0
BuildRequires:    R-CRAN-DiceKriging >= 1.5.5
BuildRequires:    R-CRAN-GenSA >= 1.1.6
BuildRequires:    R-CRAN-GPareto >= 1.0.2
BuildRequires:    R-CRAN-mco >= 1.0.15.1
BuildRequires:    R-CRAN-emoa >= 0.5.0
Requires:         R-methods >= 3.0.0
Requires:         R-CRAN-DiceKriging >= 1.5.5
Requires:         R-CRAN-GenSA >= 1.1.6
Requires:         R-CRAN-GPareto >= 1.0.2
Requires:         R-CRAN-mco >= 1.0.15.1
Requires:         R-CRAN-emoa >= 0.5.0

%description
Multi-Objective optimization based on the Kriging metamodel. Important
functions: mkm() (builder for the multiobjective models), MVPF()
(sequential minimizator using variance reduction), MEGO() (generalization
of ParEgo) and HEGO() (minimizator using the expected hypervolume
improvement). References are Passos and Luersen (2018)
<doi:10.1590/1679-78254324>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
