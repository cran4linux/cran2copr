%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RPPASPACE
%global packver   1.0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.9
Release:          1%{?dist}%{?buildtag}
Summary:          Reverse-Phase Protein Array Super Position and Concentration Evaluation

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-bmp 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-tiff 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-imager 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-cobs 
BuildRequires:    R-splines 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-SparseM 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-timeDate 
Requires:         R-methods 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-iterators 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-bmp 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-tiff 
Requires:         R-CRAN-png 
Requires:         R-CRAN-imager 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-cobs 
Requires:         R-splines 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-SparseM 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-timeDate 

%description
Provides tools for the analysis of reverse-phase protein arrays (RPPAs),
which are also known as "tissue lysate arrays" or simply "lysate arrays".
The package's primary purpose is to input a set of quantification files
representing dilution series of samples and control points taken from
scanned RPPA slides and determine a relative log concentration value for
each valid dilution series present in each slide and provide graphical
visualization of the input and output data and their relationships. Other
optional features include generation of quality control scores for judging
the quality of the input data, spatial adjustment of sample points based
on controls added to the slides, and various types of normalization of
calculated values across a set of slides. The package was derived from a
previous package named SuperCurve. For a detailed description of data
inputs and outputs, usage information, and a list of related papers
describing methods used in the package please review the vignette
"Guide_to_RPPASPACE". Hu (2007) <doi:10.1093/bioinformatics/btm283>.

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
