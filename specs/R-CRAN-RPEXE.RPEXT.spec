%global __brp_check_rpaths %{nil}
%global packname  RPEXE.RPEXT
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Reduced Piecewise Exponential Estimate/Test Software

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-stats 
Requires:         R-graphics 

%description
This reduced piecewise exponential survival software implements the
likelihood ratio test and backward elimination procedure in Han, Schell,
and Kim (2012 <doi:10.1080/19466315.2012.698945>, 2014
<doi:10.1002/sim.5915>), and Han et al. (2016 <doi:10.1111/biom.12590>).
Inputs to the program can be either times when events/censoring occur or
the vectors of total time on test and the number of events. Outputs of the
programs are times and the corresponding p-values in the backward
elimination. Details about the model and implementation are given in Han
et al. 2014. This program can run in R version 3.2.2 and above.

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
