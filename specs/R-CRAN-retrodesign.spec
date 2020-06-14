%global packname  retrodesign
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Tools for Type S (Sign) and Type M (Magnitude) Errors

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-graphics 
Requires:         R-graphics 

%description
Provides tools for working with Type S (Sign) and Type M (Magnitude)
errors, as proposed in Gelman and Tuerlinckx (2000)
<doi.org/10.1007/s001800000040> and Gelman & Carlin (2014)
<doi.org/10.1177/1745691614551642>. In addition to simply calculating the
probability of Type S/M error, the package includes functions for
calculating these errors across a variety of effect sizes for comparison,
and recommended sample size given "tolerances" for Type S/M errors. To
improve the speed of these calculations, closed forms solutions for the
probability of a Type S/M error from Lu, Qiu, and Deng (2018)
<doi.org/10.1111/bmsp.12132> are implemented. As of 1.0.0, this includes
support only for simple research designs. See the package vignette for a
fuller exposition on how Type S/M errors arise in research, and how to
analyze them using the type of design analysis proposed in the above
papers.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
