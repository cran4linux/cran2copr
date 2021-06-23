%global __brp_check_rpaths %{nil}
%global packname  dstack
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Publishing Interactive Plots

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-base64enc 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-base64enc 

%description
A native R package that allows to publish, share and track revisions of
plots using your favorite plotting package, e.g. 'ggplot2'. It also
provides a kind of interactivity for such plots by specifying certain
parameters for any specific plot view. See <https://docs.dstack.ai> for
more information.

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
