%global packname  htestClust
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Reweighted Marginal Hypothesis Tests for Clustered Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bootstrap 
BuildRequires:    R-graphics 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
Requires:         R-CRAN-bootstrap 
Requires:         R-graphics 
Requires:         R-MASS 
Requires:         R-stats 

%description
A collection of reweighted marginal hypothesis tests for clustered data,
based on reweighting methods of Williamson, J., Datta, S., and Satten, G.
(2003) <doi:10.1111/1541-0420.00005>. The tests in this collection are
clustered analogs to well-known hypothesis tests in the classical setting,
and are appropriate for data with cluster- and/or group-size
informativeness. The syntax and output of functions are modeled after
common, recognizable functions native to R. Methods used in the package
refer to Gregg, M., Datta, S., and Lorenz, D. (2020)
<doi:10.1177/0962280220928572>, Nevalainen, J., Oja, H., and Datta, S.
(2017) <doi:10.1002/sim.7288> Dutta, S. and Datta, S. (2015)
<doi:10.1111/biom.12447>, Lorenz, D., Datta, S., and Harkema, S. (2011)
<doi:10.1002/sim.4368>, Datta, S. and Satten, G. (2008)
<doi:10.1111/j.1541-0420.2007.00923.x>, Datta, S. and Satten, G. (2005)
<doi:10.1198/016214504000001583>.

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
