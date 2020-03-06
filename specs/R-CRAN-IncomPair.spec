%global packname  IncomPair
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Comparison of Means for the Incomplete Paired Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-methods 
Requires:         R-methods 

%description
Implements a variety of nonparametric and parametric methods that are
commonly used when the data set is a mixture of paired observations and
independent samples. The package also calculates and returns values of
different tests with their corresponding p-values. Bhoj, D. S. (1991)
<doi:10.1002/bimj.4710330108> "Testing equality of means in the presence
of correlation and missing data". Dubnicka, S. R., Blair, R. C., and
Hettmansperger, T. P. (2002) <doi:10.22237/jmasm/1020254460> "Rank-based
procedures for mixed paired and two-sample designs". Einsporn, R. L. and
Habtzghi, D. (2013)
<https://pdfs.semanticscholar.org/89a3/90bafeb2bc41ed4414533cfd5ab84a6b54b6.pdf>
"Combining paired and two-sample data using a permutation test". Ekbohm,
G. (1976) <doi:10.1093/biomet/63.2.299> "On comparing means in the paired
case with incomplete data on both responses". Lin, P. E. and Stivers, L.
E. (1974) <doi:10.1093/biomet/61.2.325> On difference of means with
incomplete data". Maritz, J. S. (1995)
<doi:10.1111/j.1467-842x.1995.tb00649.x> "A permutation paired test
allowing for missing values".

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
