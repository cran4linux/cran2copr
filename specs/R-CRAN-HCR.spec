%global __brp_check_rpaths %{nil}
%global packname  HCR
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Causal Discovery from Discrete Data using Hidden CompactRepresentation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.10.4
BuildRequires:    R-methods 
Requires:         R-CRAN-data.table >= 1.10.4
Requires:         R-methods 

%description
This code provides a method to fit the hidden compact representation model
as well as to identify the causal direction on discrete data. We implement
an effective solution to recover the above hidden compact representation
under the likelihood framework. Please see the Causal Discovery from
Discrete Data using Hidden Compact Representation from NIPS 2018 by Ruichu
Cai, Jie Qiao, Kun Zhang, Zhenjie Zhang and Zhifeng Hao (2018)
<https://nips.cc/Conferences/2018/Schedule?showEvent=11274> for a
description of some of our methods.

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
