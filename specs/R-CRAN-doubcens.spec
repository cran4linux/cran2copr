%global __brp_check_rpaths %{nil}
%global debug_package %{nil}
%global packname  doubcens
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Survivor Function Estimation for Doubly Interval-CensoredFailure Time Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch

%description
Contains the discrete nonparametric survivor function estimation algorithm
of De Gruttola and Lagakos for doubly interval-censored failure time data
and the discrete nonparametric survivor function estimation algorithm of
Sun for doubly interval-censored left-truncated failure time data [Victor
De Gruttola & Stephen W. Lagakos (1989) <doi:10.2307/2532030>] [Jianguo
Sun (1995) <doi:10.2307/2533008>].

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
%{rlibdir}/%{packname}
