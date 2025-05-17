%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vcd2df
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Value Change Dump to Data Frame

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Provides the 'vcd2df' function, which loads a IEEE 1364-1995/2001 VCD
(.vcd) file, specified as a parameter of type string containing exactly a
file path, and returns an R dataframe containing values over time. A VCD
file captures the register values at discrete timepoints from a simulated
trace of execution of a hardware design in Verilog or VHDL. The returned
dataframe contains a row for each register, by name, and a column for each
time point, specified VCD-style using octothorpe-prefixed multiples of the
timescale as strings. The only non-trivial implementation details are that
(1) VCD 'x' and 'z' non-numerical values are encoded as negative value -1
(as otherwise all bit values are positive) and (2) registers with repeated
names in distinct modules are ignored, rather than duplicated, as we
anticipate these registers to have the same values. Read more in arXiv
preprint: 'vcd2df' -- Leveraging Data Science Insights for Hardware
Security Research <doi:10.48550/arXiv.2505.06470>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
