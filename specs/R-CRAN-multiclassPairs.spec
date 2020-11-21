%global packname  multiclassPairs
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Build MultiClass Pair-Based Classifiers using TSPs or RF

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-Boruta 
BuildRequires:    R-CRAN-dunn.test 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-rdist 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-Boruta 
Requires:         R-CRAN-dunn.test 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-rdist 

%description
A toolbox to train a single sample classifier that uses in-sample feature
relationships. The relationships are represented as feature1 < feature2
(e.g. gene1 < gene2). We provide two options to go with. First is based on
'switchBox' package which uses Top-score pairs algorithm. Second is a
novel implementation based on random forest algorithm. For simple problems
we recommend to use one-vs-rest using TSP option due to its simplicity and
for being easy to interpret.  For complex problems RF performs better.
Both lines filter the features first then combine the filtered features to
make the list of all the possible rules (i.e. rule1: feature1 < feature2,
rule2: feature1 < feature3, etc...).  Then the list of rules will be
filtered and the most important and informative rules will be kept. The
informative rules will be assembled in an one-vs-rest model or in an RF
model.  We provide a detailed description with each function in this
package to explain the filtration and training methodology in each line.

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
