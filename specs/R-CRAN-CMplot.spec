%global packname  CMplot
%global packver   3.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.6.2
Release:          2%{?dist}%{?buildtag}
Summary:          Circle Manhattan Plot

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
Manhattan plot, a type of scatter plot, was widely used to display the
association results. However, it is usually time-consuming and laborious
for a non-specialist user to write scripts and adjust parameters of an
elaborate plot. Moreover, the ever-growing traits measured have
necessitated the integration of results from different Genome-wide
association study researches. Circle Manhattan Plot is the first open R
package that can lay out. Genome-wide association study P-value results in
both traditional rectangular patterns, QQ-plot and novel circular ones.
United in only one bull's eye style plot, association results from
multiple traits can be compared interactively, thereby to reveal both
similarities and differences between signals. Additional functions
include: highlight signals, a group of SNPs, chromosome visualization and
candidate genes around SNPs.

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
