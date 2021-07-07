%global __brp_check_rpaths %{nil}
%global packname  spreval
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Evaluation of Sprinkler Irrigation Uniformity and Efficiency

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-timeDate 
BuildRequires:    R-CRAN-interp 
Requires:         R-CRAN-timeDate 
Requires:         R-CRAN-interp 

%description
Processing and analysis of field collected or simulated sprinkler system
catch data (depths) to characterize irrigation uniformity and efficiency
using standard and other measures. Standard measures include the
Christiansen coefficient of uniformity (CU) as found in Christiansen,
J.E.(1942, ISBN:0138779295, "Irrigation by Sprinkling"); and distribution
uniformity (DU), potential efficiency of the low quarter (PELQ), and
application efficiency of the low quarter (AELQ) that are implementations
of measures of the same notation in Keller, J. and Merriam, J.L. (1978)
"Farm Irrigation System Evaluation: A Guide for Management"
<https://pdf.usaid.gov/pdf_docs/PNAAG745.pdf>. spreval::DU.lh is similar
to spreval::DU but is the distribution uniformity of the low half instead
of low quarter as in DU. spreval::PELQT is a version of spreval::PELQ
adapted for traveling systems instead of lateral move or solid-set
sprinkler systems. The function spreval::eff is analogous to the method
used to compute application efficiency for furrow irrigation presented in
Walker, W. and Skogerboe, G.V. (1987,ISBN:0138779295, "Surface Irrigation:
Theory and Practice"),that uses piecewise integration of infiltrated depth
compared against soil-moisture deficit (SMD), when the argument "target"
is set equal to SMD.  The other functions contained in the package provide
graphical representation of sprinkler system uniformity, and other
standard univariate parametric and non-parametric statistical measures as
applied to sprinkler system catch depths. A sample data set of field test
data spreval::catchcan (catch depths) is provided and is used in examples
and vignettes.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
