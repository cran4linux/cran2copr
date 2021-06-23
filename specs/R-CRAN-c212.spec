%global __brp_check_rpaths %{nil}
%global packname  c212
%global packver   0.98
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.98
Release:          1%{?dist}%{?buildtag}
Summary:          Methods for Detecting Safety Signals in Clinical Trials Using Body-Systems (System Organ Classes)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-coda 
Requires:         R-CRAN-coda 

%description
Methods for detecting safety signals in clinical trials using groupings of
adverse events by body-system or system organ class. This work was
supported by the Engineering and Physical Sciences Research Council (UK)
(EPSRC) [award reference 1521741] and Frontier Science (Scotland) Ltd. The
package title c212 is in reference to the original Engineering and
Physical Sciences Research Council (UK) funded project which was named
CASE 2/12.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
