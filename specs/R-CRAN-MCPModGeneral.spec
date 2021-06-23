%global __brp_check_rpaths %{nil}
%global packname  MCPModGeneral
%global packver   0.1-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          A Supplement to the 'DoseFinding' Package for the General Case

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-DoseFinding 
BuildRequires:    R-stats 
BuildRequires:    R-MASS 
Requires:         R-CRAN-DoseFinding 
Requires:         R-stats 
Requires:         R-MASS 

%description
Analyzes non-normal data via the Multiple Comparison Procedures and
Modeling approach (MCP-Mod). Many functions rely on the 'DoseFinding'
package. This package makes it so the user does not need to provide or
calculate the mu vector and S matrix. Instead, the user typically supplies
the data in its raw form, and this package will calculate the needed
objects and passes them into the 'DoseFinding' functions. If the user
wishes to primarily use the functions provided in the 'DoseFinding'
package, a singular function (prepareGen()) will provide mu and S. The
package currently handles power analysis and the MCP-Mod procedure for
negative binomial, Poisson, and binomial data. The MCP-Mod procedure can
also be applied to survival data, but power analysis is not available.
Bretz, F., Pinheiro, J. C., and Branson, M. (2005)
<doi:10.1111/j.1541-0420.2005.00344.x>. Buckland, S. T., Burnham, K. P.
and Augustin, N. H. (1997) <doi:10.2307/2533961>. Pinheiro, J. C.,
Bornkamp, B., Glimm, E. and Bretz, F. (2014) <doi:10.1002/sim.6052>.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
