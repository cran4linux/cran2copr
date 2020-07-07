%global packname  lolR
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          2%{?dist}
Summary:          Linear Optimal Low-Rank Projection

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-robust 
BuildRequires:    R-CRAN-robustbase 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-abind 
Requires:         R-MASS 
Requires:         R-CRAN-irlba 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-robust 
Requires:         R-CRAN-robustbase 

%description
Supervised learning techniques designed for the situation when the
dimensionality exceeds the sample size have a tendency to overfit as the
dimensionality of the data increases. To remedy this High dimensionality;
low sample size (HDLSS) situation, we attempt to learn a lower-dimensional
representation of the data before learning a classifier. That is, we
project the data to a situation where the dimensionality is more
manageable, and then are able to better apply standard classification or
clustering techniques since we will have fewer dimensions to overfit. A
number of previous works have focused on how to strategically reduce
dimensionality in the unsupervised case, yet in the supervised HDLSS
regime, few works have attempted to devise dimensionality reduction
techniques that leverage the labels associated with the data. In this
package and the associated manuscript Vogelstein et al. (2017)
<arXiv:1709.01233>, we provide several methods for feature extraction,
some utilizing labels and some not, along with easily extensible utilities
to simplify cross-validative efforts to identify the best feature
extraction method. Additionally, we include a series of adaptable
benchmark simulations to serve as a standard for future investigative
efforts into supervised HDLSS. Finally, we produce a comprehensive
comparison of the included algorithms across a range of benchmark
simulations and real data applications.

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
