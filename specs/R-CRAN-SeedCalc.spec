%global __brp_check_rpaths %{nil}
%global packname  SeedCalc
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Seed Germination and Seedling Growth Indexes

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Functions to calculate seed germination and seedling emergence and growth
indexes. The main indexes for germination and seedling emergence,
considering the time for seed germinate are: T10, T50 and T90, in Farooq
et al. (2005) <10.1111/j.1744-7909.2005.00031.x>; and MGT, in Labouriau
(1983). Considering the germination speed are: Germination Speed Index, in
Maguire (1962), Mean Germination Rate, in Labouriau (1983); considering
the homogeneity of germination are: Coefficient of Variation of the
Germination Time, in Carvalho et al. (2005)
<10.1590/S0100-84042005000300018>, and Variance of Germination, in
Labouriau (1983); Uncertainty, in Labouriau and Valadares (1976)
<ISSN:0001-3765>; and Synchrony, in Primack (1980). The main seedling
indexes are Growth, in Sako (2001), Uniformity, in Sako (2001) and Castan
et al. (2018) <doi:10.1590/1678-992x-2016-0401>; and Vigour, in Medeiros
and Pereira (2018) <doi:10.1590/1983-40632018v4852340>.

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
