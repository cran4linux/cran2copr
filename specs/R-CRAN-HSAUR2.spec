%global packname  HSAUR2
%global packver   1.1-18
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.18
Release:          1%{?dist}%{?buildtag}
Summary:          A Handbook of Statistical Analyses Using R (2nd Edition)

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.2.0
Requires:         R-core >= 2.2.0
BuildArch:        noarch
BuildRequires:    R-tools 
Requires:         R-tools 

%description
Functions, data sets, analyses and examples from the second edition of the
book ''A Handbook of Statistical Analyses Using R'' (Brian S. Everitt and
Torsten Hothorn, Chapman & Hall/CRC, 2008). The first chapter of the book,
which is entitled ''An Introduction to R'', is completely included in this
package, for all other chapters, a vignette containing all data analyses
is available. In addition, the package contains Sweave code for producing
slides for selected chapters (see HSAUR2/inst/slides).

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
