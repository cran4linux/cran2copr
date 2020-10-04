%global packname  ROP
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Regression Optimized: Numerical Approach for MultivariateClassification and Regression Trees

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ROCR 
Requires:         R-CRAN-ROCR 

%description
Trees Classification and Regression using multivariate nodes calculated by
an exhaustive numerical approach. We propose a new concept of decision
tree, including multivariate knots and non hierarchical pathway. This
package's model uses a multivariate nodes tree that calculates directly a
risk score for each observation for the state Y observed. Nguyen JM,
Gaultier A, Antonioli D (2015) <doi:10.1016/j.respe.2018.03.088> Castillo
JM, Knol AC, Nguyen JM, Khammari A, Saint Jean M, Dreno B (2016)
<doi:10.1684/ejd.2016.2826> Vildy S, Nguyen JM, Gaultier A, Khammari A,
Dreno B (2017) <doi:10.1684/ejd.2016.2955> Nguyen JM, Gaultier A,
Antonioli D (2018) <doi:10.1016/j.respe.2018.03.088>.

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
