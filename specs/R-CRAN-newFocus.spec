%global __brp_check_rpaths %{nil}
%global packname  newFocus
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          True Discovery Guarantee by the New Focus Level Procedure

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ctgt 
Requires:         R-CRAN-ctgt 

%description
A new focus level procedure is developed based on the old focus level
procedure of Goeman and Mansmann (2008)
<doi:10.1093/bioinformatics/btm628> and the closed testing procedure with
globaltest of Xu and Goeman (2020) <arXiv:2001.01541>. It produces the
lower bound for the number of true discoveries in any gene set or GO (Gene
Ontology) term. It is more powerful for the focus level GO terms chosen by
user before seeing the data than the non-focus level GO terms or gene sets
chosen after seeing the data.

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
