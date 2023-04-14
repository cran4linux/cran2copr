%global __brp_check_rpaths %{nil}
%global packname  coppeCosenzaR
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          COPPE-Cosenza Fuzzy Hierarchy Model

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-methods 
Requires:         R-methods 

%description
The program implements the COPPE-Cosenza Fuzzy Hierarchy Model. The model
was based on the evaluation of local alternatives, representing regional
potentialities, so as to fulfill demands of economic projects. After
defining demand profiles in terms of their technological coefficients, the
degree of importance of factors is defined so as to represent the
productive activity. The method can detect a surplus of supply without the
restriction of the distance of classical algebra, defining a hierarchy of
location alternatives. In COPPE-Cosenza Model, the distance between
factors is measured in terms of the difference between grades of
memberships of the same factors belonging to two or more sets under
comparison. The required factors are classified under the following
linguistic variables: Critical (CR); Conditioning (C); Little Conditioning
(LC); and Irrelevant (I). And the alternatives can assume the following
linguistic variables: Excellent (Ex), Good (G), Regular (R), Weak (W),
Empty (Em), Zero (Z) and Inexistent (In). The model also provides
flexibility, allowing different aggregation rules to be performed and
defined by the Decision Maker. Such feature is considered in this package,
allowing the user to define other aggregation matrices, since it considers
the same linguistic variables mentioned.

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
