%global __brp_check_rpaths %{nil}
%global packname  GMDHreg
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Regression using GMDH Algorithms

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15
Requires:         R-core >= 2.15
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-utils 

%description
Regression using GMDH algorithms from Prof. Alexey G. Ivakhnenko. Group
Method of Data Handling (GMDH), or polynomial neural networks, is a family
of inductive algorithms that performs gradually complicated polynomial
models and selecting the best solution by an external criterion. In other
words, inductive GMDH algorithms give possibility finding automatically
interrelations in data, and selecting an optimal structure of model or
network. The package includes GMDH Combinatorial, GMDH MIA (Multilayered
Iterative Algorithm), GMDH GIA (Generalized Iterative Algorithm) and GMDH
Combinatorial with Active Neurons. An introduction of GMDH algorithms:
Farlow, S.J. (1981): "The GMDH algorithm of Ivakhnenko", The American
Statistician, 35(4), pp. 210-215. <doi:10.2307/2683292> Ivakhnenko A.G.
(1968): "The Group Method of Data Handling - A Rival of the Method of
Stochastic Approximation", Soviet Automatic Control, 13(3), pp. 43-55.

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
