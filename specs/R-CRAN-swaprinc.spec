%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  swaprinc
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Swap Principal Components into Regression Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-broom.mixed 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Gifi 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-broom.mixed 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Gifi 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyselect 

%description
Obtaining accurate and stable estimates of regression coefficients can be
challenging when the suggested statistical model has issues related to
multicollinearity, convergence, or overfitting. One solution is to use
principal component analysis (PCA) results in the regression, as discussed
in Chan and Park (2005) <doi:10.1080/01446190500039812>. The swaprinc()
package streamlines comparisons between a raw regression model with the
full set of raw independent variables and a principal component regression
model where principal components are estimated on a subset of the
independent variables, then swapped into the regression model in place of
those variables. The swaprinc() function compares one raw regression model
to one principal component regression model, while the compswap() function
compares one raw regression model to many principal component regression
models. Package functions include parameters to center, scale, and undo
centering and scaling, as described by Harvey and Hansen (2022)
<https://cran.r-project.org/package=LearnPCA/vignettes/Vig_03_Step_By_Step_PCA.pdf>.
Additionally, the package supports using Gifi methods to extract principal
components from categorical variables, as outlined by Rossiter (2021)
<https://www.css.cornell.edu/faculty/dgr2/_static/files/R_html/NonlinearPCA.html#2_Package>.

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
