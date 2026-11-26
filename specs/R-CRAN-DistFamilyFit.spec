%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DistFamilyFit
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Fitting and Comparing Flexible Continuous Distribution Families

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 

%description
Fits and compares four flexible families of continuous distributions, with
the Johnson family as the default. Pearson curves described by Pearson
(1895) <doi:10.1098/rsta.1895.0010> are fitted by four-moment matching
through 'PearsonDS'. The unbounded (SU), lognormal (SL) and bounded (SB)
translation systems of Johnson (1949) <doi:10.1093/biomet/36.1-2.149> are
fitted by profiled numerical maximum likelihood, and Burr Type III and
Type XII distributions of Burr (1942) <doi:10.1214/aoms/1177731607>, see
also Tadikamalla (1980) <doi:10.2307/1402945>, by numerical maximum
likelihood. The generalized lambda distribution of Ramberg and Schmeiser
(1974) <doi:10.1145/360827.360840> is used in the parameterization of
Freimer, Kollia, Mudholkar and Lin (1988) <doi:10.1080/03610928808829820>
and is fitted by quantile matching with numerical inversion of its
quantile function. Candidates are ranked by descriptive distances between
fitted and empirical cumulative distribution functions. Johnson marginal
transformations to a common normal scale support descriptive dependence
analysis without implying joint normality on the original scale. The
package also provides numeric data validation with row-level audits,
density, distribution and quantile evaluation, and separate plotting
functions. Count data are treated as continuous approximations. The
methodology and its application to mobile application usage data are
described in Karakaya Demir, Purutçuoğlu and Bursalı (2026), accepted at
the 3rd International Conference on Advanced Technology in Electronic and
Electrical Engineering (ICATEEE 2026).

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
