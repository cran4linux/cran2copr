%global packname  reinforcelearn
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          2%{?dist}
Summary:          Reinforcement Learning

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-nnet >= 7.3.12
BuildRequires:    R-CRAN-R6 >= 2.2.2
BuildRequires:    R-CRAN-checkmate >= 1.8.4
BuildRequires:    R-CRAN-purrr >= 0.2.4
Requires:         R-nnet >= 7.3.12
Requires:         R-CRAN-R6 >= 2.2.2
Requires:         R-CRAN-checkmate >= 1.8.4
Requires:         R-CRAN-purrr >= 0.2.4

%description
Implements reinforcement learning environments and algorithms as described
in Sutton & Barto (1998, ISBN:0262193981). The Q-Learning algorithm can be
used with function approximation, eligibility traces (Singh & Sutton
(1996) <doi:10.1007/BF00114726>) and experience replay (Mnih et al. (2013)
<arXiv:1312.5602>).

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
