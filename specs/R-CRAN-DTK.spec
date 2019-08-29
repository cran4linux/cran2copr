%global packname  DTK
%global packver   3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.5
Release:          1%{?dist}
Summary:          Dunnett-Tukey-Kramer Pairwise Multiple Comparison Test Adjustedfor Unequal Variances and Unequal Sample Sizes

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
This package was created to analyze multi-level one-way experimental
designs. It is designed to handle vectorized observation and factor data
where there are unequal sample sizes and population variance homogeneity
can not be assumed. To conduct the Dunnett modified Tukey-Kramer test
(a.k.a. the T3 Procedure), create two vectors: one for your observations
and one for the factor level of each observation. The function,
gl.unequal, provides a means to more conveniently produce a factor vector
with unequal sample sizes. Next, use the DTK.test function to conduct the
test and save the output as an object to input into the DTK.plot function,
which produces a confidence interval plot for each of the pairwise
comparisons. Lastly, the function TK.test conducts the original
Tukey-Kramer test.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
