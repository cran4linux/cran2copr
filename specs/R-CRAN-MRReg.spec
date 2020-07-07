%global packname  MRReg
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}
Summary:          MDL Multiresolution Linear Regression Framework

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-igraph 
Requires:         R-CRAN-ggplot2 >= 3.0
Requires:         R-CRAN-caret 
Requires:         R-CRAN-igraph 

%description
We provide the framework to analyze multiresolution partitions (e.g.
country, provinces, subdistrict) where each individual data point belongs
to only one partition in each layer (e.g. i belongs to subdistrict A,
province P, and country Q).  We assume that a partition in a higher layer
subsumes lower-layer partitions (e.g. a nation is at the 1st layer
subsumes all provinces at the 2nd layer). Given N individuals that have a
pair of real values (x,y) that generated from independent variable X and
dependent variable Y. Each individual i belongs to one partition per
layer. Our goal is to find which partitions at which highest level that
all individuals in the these partitions share the same linear model Y=f(X)
where f is a linear function. The framework deploys the Minimum
Description Length principle (MDL) to infer solutions. The publication of
this package is at Chainarong Amornbunchornvej, Navaporn Surasvadi, Anon
Plangprasopchok, and Suttipong Thajchayapong (2019) <arXiv:1907.05234>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
