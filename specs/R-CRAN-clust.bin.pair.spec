%global __brp_check_rpaths %{nil}
%global packname  clust.bin.pair
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Statistical Methods for Analyzing Clustered Matched Pair Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.4
Requires:         R-core >= 3.2.4
BuildArch:        noarch

%description
Tests, utilities, and case studies for analyzing significance in clustered
binary matched-pair data. The central function clust.bin.pair uses one of
several tests to calculate a Chi-square statistic. Implemented are the
tests Eliasziw (1991) <doi:10.1002/sim.4780101211>, Obuchowski (1998)
<doi:10.1002/(SICI)1097-0258(19980715)17:13%3C1495::AID-SIM863%3E3.0.CO;2-I>,
Durkalski (2003) <doi:10.1002/sim.1438>, and Yang (2010)
<doi:10.1002/bimj.201000035> with McNemar (1947) <doi:10.1007/BF02295996>
included for comparison. The utility functions nested.to.contingency and
paired.to.contingency convert data between various useful formats.
Thyroids and psychiatry are the canonical datasets from Obuchowski and
Petryshen (1989) <doi:10.1016/0165-1781(89)90196-0> respectively.

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
