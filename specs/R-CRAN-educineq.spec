%global __brp_check_rpaths %{nil}
%global packname  educineq
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Compute and Decompose Inequality in Education

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ineq 
BuildRequires:    R-CRAN-flexsurv 
Requires:         R-CRAN-ineq 
Requires:         R-CRAN-flexsurv 

%description
Easily compute education inequality measures and the distribution of
educational attainments for any group of countries, using the data set
developed in Jorda, V. and Alonso, JM. (2017)
<DOI:10.1016/j.worlddev.2016.10.005>. The package offers the possibility
to compute not only the Gini index, but also generalized entropy measures
for different values of the sensitivity parameter. In particular, the
package includes functions to compute the mean log deviation, which is
more sensitive to the bottom part of the distribution; the Theil’s entropy
measure, equally sensitive to all parts of the distribution; and finally,
the GE measure when the sensitivity parameter is set equal to 2, which
gives more weight to differences in higher education. The decomposition of
these measures in the components between-country and within-country
inequality is also provided. Two graphical tools are also provided, to
analyse the evolution of the distribution of educational attainments: The
cumulative distribution function and the Lorenz curve.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
