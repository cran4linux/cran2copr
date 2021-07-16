%global __brp_check_rpaths %{nil}
%global packname  iMRMC
%global packver   1.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Multi-Reader, Multi-Case Analysis Methods (ROC, Agreement, and Other Metrics)

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Do Multi-Reader, Multi-Case (MRMC) analyses of data from imaging studies
where clinicians (readers) evaluate patient images (cases). What does this
mean? ... Many imaging studies are designed so that every reader reads
every case in all modalities, a fully-crossed study. In this case, the
data is cross-correlated, and we consider the readers and cases to be
cross-correlated random effects. An MRMC analysis accounts for the
variability and correlations from the readers and cases when estimating
variances, confidence intervals, and p-values. The functions in this
package can treat arbitrary study designs and studies with missing data,
not just fully-crossed study designs. The initial package analyzes the
reader-average area under the receiver operating characteristic (ROC)
curve with U-statistics according to Gallas, Bandos, Samuelson, and Wagner
2009 <doi:10.1080/03610920802610084>. Additional functions analyze other
endpoints with U-statistics (binary performance and score differences)
following the work by Gallas, Pennello, and Myers 2007
<doi:10.1364/JOSAA.24.000B70>. Package development and documentation is at
<https://github.com/DIDSR/iMRMC/tree/master>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
