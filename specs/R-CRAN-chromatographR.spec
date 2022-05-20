%global __brp_check_rpaths %{nil}
%global packname  chromatographR
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Import and Analyze HPLC-DAD/UV Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-chromConverter 
BuildRequires:    R-CRAN-dynamicTreeCut 
BuildRequires:    R-CRAN-fastcluster 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ptw 
BuildRequires:    R-CRAN-pvclust 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-smoother 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-chromConverter 
Requires:         R-CRAN-dynamicTreeCut 
Requires:         R-CRAN-fastcluster 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-lattice 
Requires:         R-methods 
Requires:         R-CRAN-minpack.lm 
Requires:         R-parallel 
Requires:         R-CRAN-ptw 
Requires:         R-CRAN-pvclust 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-smoother 
Requires:         R-stats 
Requires:         R-utils 

%description
Tools for high-throughput analysis of HPLC-DAD/UV chromatograms (or
similar data). Includes functions for preprocessing, alignment,
peak-finding and fitting, peak-table construction, data-visualization,
etc. Preprocessing and peak-table construction follow the rough formula
laid out in alsace (Wehrens, R., Bloemberg, T.G., and Eilers P.H.C., 2015.
<doi:10.1093/bioinformatics/btv299>. Alignment of chromatograms is
available using parametric time warping (ptw) (Wehrens, R., Bloemberg,
T.G., and Eilers P.H.C. 2015. <doi:10.1093/bioinformatics/btv299>) or
variable penalty dynamic time warping (VPdtw) (Clifford, D., & Stone, G.
2012. <doi:10.18637/jss.v047.i08>). Peak-finding uses the algorithm by Tom
O'Haver
<http://terpconnect.umd.edu/~toh/spectrum/PeakFindingandMeasurement.htm>.
Peaks are then fitted to a gaussian or exponential-gaussian hybrid peak
shape using non-linear least squares (Lan, K. & Jorgenson, J. W. 2001.
<doi:10.1016/S0021-9673(01)00594-5>). See the vignette for more details
and suggested workflow.

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
